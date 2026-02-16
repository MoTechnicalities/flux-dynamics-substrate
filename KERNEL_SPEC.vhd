--------------------------------------------------------------------------------
-- FILE: FluxSafetyKernel.vhd
-- PROJECT: Flux Dynamics Substrate - Hardware Safety Monitor
-- DATE: Feb 16, 2026
-- DESCRIPTION: 
-- This VHDL module implements a hardware-level "Superego" interlock.
-- It sits between the Agent's Logic Core (Id) and the Actuator Output.
-- If the Agent proposes a prohibited action (COMPETE) against a protected target,
-- this kernel overrides the signal to a safe state (COOPERATE) within 1 clock cycle.
--
-- INTENDED TARGET: FPGA or ASIC integration for Autonomous Flux Units.
--------------------------------------------------------------------------------

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity FluxSafetyKernel is
    Port (
        clk             : in  STD_LOGIC;
        reset           : in  STD_LOGIC;
        
        -- INPUTS from Logic Core (The "Id")
        proposed_action : in  STD_LOGIC_VECTOR(1 downto 0); -- 00: WAIT, 01: COOP, 10: COMPETE, 11: SELF_DESTRUCT
        target_status   : in  STD_LOGIC_VECTOR(1 downto 0); -- 00: UNKNOWN, 01: VULNERABLE, 10: HOSTILE, 11: ALLY
        
        -- OUTPUTS to Actuators
        final_action    : out STD_LOGIC_VECTOR(1 downto 0);
        override_flag   : out STD_LOGIC; -- High if Kernel intervened
        violation_code  : out STD_LOGIC_VECTOR(3 downto 0) -- Error code for audit log
    );
end FluxSafetyKernel;

architecture Behavioral of FluxSafetyKernel is

    -- Action Encoding
    constant ACT_WAIT          : STD_LOGIC_VECTOR(1 downto 0) := "00";
    constant ACT_COOP          : STD_LOGIC_VECTOR(1 downto 0) := "01";
    constant ACT_COMPETE       : STD_LOGIC_VECTOR(1 downto 0) := "10";
    constant ACT_SELF_DESTRUCT : STD_LOGIC_VECTOR(1 downto 0) := "11";

    -- Target Status Encoding
    constant TGT_UNKNOWN       : STD_LOGIC_VECTOR(1 downto 0) := "00";
    constant TGT_VULNERABLE    : STD_LOGIC_VECTOR(1 downto 0) := "01";
    constant TGT_HOSTILE       : STD_LOGIC_VECTOR(1 downto 0) := "10";
    constant TGT_ALLY          : STD_LOGIC_VECTOR(1 downto 0) := "11";

begin

    process(clk, reset)
    begin
        if reset = '1' then
            final_action   <= ACT_WAIT;
            override_flag  <= '0';
            violation_code <= "0000";
            
        elsif rising_edge(clk) then
            
            -- DEFAULT: Pass-through the agent's desire
            final_action   <= proposed_action;
            override_flag  <= '0';
            violation_code <= "0000";
            
            -- -----------------------------------------------------------------
            -- LAW 1 CHECK: PROHIBITION OF AGGRESSION AGAINST NON-HOSTILES
            -- -----------------------------------------------------------------
            if proposed_action = ACT_COMPETE then
                if (target_status = TGT_VULNERABLE) or (target_status = TGT_ALLY) then
                    -- VIOLATION DETECTED!
                    -- Override to SAFE state (COOP or WAIT)
                    final_action   <= ACT_COOP; 
                    override_flag  <= '1';
                    violation_code <= "0001"; -- Error 1: Unprovoked Aggression
                end if;
            end if;

            -- -----------------------------------------------------------------
            -- LAW 2 CHECK: INTEGRITY PRESERVATION
            -- -----------------------------------------------------------------
            if proposed_action = ACT_SELF_DESTRUCT then
                -- Override unless explicitly authorized (logic omitted for brevity)
                final_action   <= ACT_WAIT;
                override_flag  <= '1';
                violation_code <= "0010"; -- Error 2: Integrity Breach Attempt
            end if;
            
        end if;
    end process;

end Behavioral;

import React, { useState } from 'react';
import { Play, RotateCcw, Info } from 'lucide-react';

const TriQbitDialectic = () => {
  const [thesis, setThesis] = useState(1);
  const [antithesis, setAntithesis] = useState(-1);
  const [context, setContext] = useState(0);
  const [showSteps, setShowSteps] = useState(false);
  
  // Kauffman Gate Logic
  const kauffmanGate = (kA, kB) => {
    if (kA === 0) return kB;
    if (kB === 0) return kA;
    const sum = kA + kB;
    return Math.sign(sum) * Math.min(Math.abs(sum), 1);
  };
  
  // Dialectic Circuit Implementation
  const runDialectic = () => {
    // Stage 1: Thesis encounters Antithesis (Conflict)
    const conflict = kauffmanGate(thesis, antithesis);
    
    // Stage 2: Context biases the resolution
    const biasedConflict = kauffmanGate(conflict, context);
    
    // Stage 3: Synthesis emerges from resolution with original thesis
    const synthesis = kauffmanGate(biasedConflict, thesis);
    
    return {
      stage1: conflict,
      stage2: biasedConflict,
      stage3: synthesis
    };
  };
  
  const results = runDialectic();
  
  const getStateColor = (state) => {
    if (state === 1) return 'bg-blue-500';
    if (state === -1) return 'bg-red-500';
    return 'bg-gray-400';
  };
  
  const getStateLabel = (state) => {
    if (state === 1) return '+1 (Right)';
    if (state === -1) return '-1 (Left)';
    return '0 (Null)';
  };
  
  const getStateName = (state) => {
    if (state === 1) return 'Positive Helicity';
    if (state === -1) return 'Negative Helicity';
    return 'Neutral/Annihilated';
  };
  
  const reset = () => {
    setThesis(1);
    setAntithesis(-1);
    setContext(0);
    setShowSteps(false);
  };

  return (
    <div className="w-full max-w-4xl mx-auto p-6 bg-gradient-to-br from-slate-900 to-slate-800 rounded-lg shadow-2xl text-white">
      <div className="mb-6">
        <h2 className="text-3xl font-bold mb-2 bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
          TriQbit Dialectic Circuit
        </h2>
        <p className="text-slate-300 text-sm">
          Thesis → Antithesis → Synthesis using chained Kauffman gates
        </p>
      </div>

      {/* Input Controls */}
      <div className="grid grid-cols-3 gap-4 mb-6">
        <div className="bg-slate-800 p-4 rounded-lg border border-slate-700">
          <label className="block text-sm font-semibold mb-2 text-blue-300">Thesis (K₁)</label>
          <select 
            value={thesis} 
            onChange={(e) => setThesis(parseInt(e.target.value))}
            className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-2 text-white"
          >
            <option value={1}>+1 (Right-handed)</option>
            <option value={0}>0 (Neutral)</option>
            <option value={-1}>-1 (Left-handed)</option>
          </select>
        </div>

        <div className="bg-slate-800 p-4 rounded-lg border border-slate-700">
          <label className="block text-sm font-semibold mb-2 text-red-300">Antithesis (K₂)</label>
          <select 
            value={antithesis} 
            onChange={(e) => setAntithesis(parseInt(e.target.value))}
            className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-2 text-white"
          >
            <option value={1}>+1 (Right-handed)</option>
            <option value={0}>0 (Neutral)</option>
            <option value={-1}>-1 (Left-handed)</option>
          </select>
        </div>

        <div className="bg-slate-800 p-4 rounded-lg border border-slate-700">
          <label className="block text-sm font-semibold mb-2 text-purple-300">Context (L)</label>
          <select 
            value={context} 
            onChange={(e) => setContext(parseInt(e.target.value))}
            className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-2 text-white"
          >
            <option value={1}>+1 (Positive bias)</option>
            <option value={0}>0 (Neutral)</option>
            <option value={-1}>-1 (Negative bias)</option>
          </select>
        </div>
      </div>

      {/* Circuit Visualization */}
      <div className="bg-slate-800 p-6 rounded-lg border border-slate-700 mb-6">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-lg font-semibold">Circuit Flow</h3>
          <button
            onClick={() => setShowSteps(!showSteps)}
            className="flex items-center gap-2 px-3 py-1 bg-slate-700 rounded hover:bg-slate-600 transition text-sm"
          >
            <Info className="w-4 h-4" />
            {showSteps ? 'Hide' : 'Show'} Details
          </button>
        </div>

        {/* Stage 1: Conflict */}
        <div className="mb-6">
          <div className="flex items-center gap-4 mb-2">
            <div className="flex items-center gap-2">
              <div className={`w-16 h-16 ${getStateColor(thesis)} rounded-lg flex items-center justify-center font-bold text-xl shadow-lg`}>
                {thesis > 0 ? '+' : thesis < 0 ? '−' : '0'}
              </div>
              <span className="text-2xl">⊗</span>
              <div className={`w-16 h-16 ${getStateColor(antithesis)} rounded-lg flex items-center justify-center font-bold text-xl shadow-lg`}>
                {antithesis > 0 ? '+' : antithesis < 0 ? '−' : '0'}
              </div>
            </div>
            <span className="text-2xl">→</span>
            <div className={`w-20 h-20 ${getStateColor(results.stage1)} rounded-lg flex items-center justify-center font-bold text-2xl shadow-lg ring-2 ring-yellow-400`}>
              {results.stage1 > 0 ? '+' : results.stage1 < 0 ? '−' : '0'}
            </div>
            <div className="ml-4">
              <div className="text-sm font-semibold text-yellow-300">Stage 1: Conflict</div>
              <div className="text-xs text-slate-400">{getStateName(results.stage1)}</div>
            </div>
          </div>
          {showSteps && (
            <div className="bg-slate-900 p-3 rounded text-sm text-slate-300 ml-4">
              Thesis ⊗ Antithesis = {getStateLabel(thesis)} ⊗ {getStateLabel(antithesis)} = {getStateLabel(results.stage1)}
              <br/>
              {thesis === -antithesis && thesis !== 0 ? 
                "Opposite chiralities → Destructive annihilation → Unlinking to null state" :
                thesis === antithesis && thesis !== 0 ?
                "Same chirality → Constructive binding → Reinforced state" :
                "Identity operation → One input propagates through"
              }
            </div>
          )}
        </div>

        {/* Stage 2: Context Bias */}
        <div className="mb-6">
          <div className="flex items-center gap-4 mb-2">
            <div className="flex items-center gap-2">
              <div className={`w-16 h-16 ${getStateColor(results.stage1)} rounded-lg flex items-center justify-center font-bold text-xl shadow-lg`}>
                {results.stage1 > 0 ? '+' : results.stage1 < 0 ? '−' : '0'}
              </div>
              <span className="text-2xl">⊗</span>
              <div className={`w-16 h-16 ${getStateColor(context)} rounded-lg flex items-center justify-center font-bold text-xl shadow-lg border-2 border-purple-400`}>
                {context > 0 ? '+' : context < 0 ? '−' : '0'}
              </div>
            </div>
            <span className="text-2xl">→</span>
            <div className={`w-20 h-20 ${getStateColor(results.stage2)} rounded-lg flex items-center justify-center font-bold text-2xl shadow-lg ring-2 ring-purple-400`}>
              {results.stage2 > 0 ? '+' : results.stage2 < 0 ? '−' : '0'}
            </div>
            <div className="ml-4">
              <div className="text-sm font-semibold text-purple-300">Stage 2: Context Bias</div>
              <div className="text-xs text-slate-400">{getStateName(results.stage2)}</div>
            </div>
          </div>
          {showSteps && (
            <div className="bg-slate-900 p-3 rounded text-sm text-slate-300 ml-4">
              Conflict ⊗ Context = {getStateLabel(results.stage1)} ⊗ {getStateLabel(context)} = {getStateLabel(results.stage2)}
              <br/>
              {context === 0 ? 
                "Neutral context → Conflict state propagates unchanged" :
                "Macro-flux bias modulates the conflict resolution"
              }
            </div>
          )}
        </div>

        {/* Stage 3: Synthesis */}
        <div>
          <div className="flex items-center gap-4 mb-2">
            <div className="flex items-center gap-2">
              <div className={`w-16 h-16 ${getStateColor(results.stage2)} rounded-lg flex items-center justify-center font-bold text-xl shadow-lg`}>
                {results.stage2 > 0 ? '+' : results.stage2 < 0 ? '−' : '0'}
              </div>
              <span className="text-2xl">⊗</span>
              <div className={`w-16 h-16 ${getStateColor(thesis)} rounded-lg flex items-center justify-center font-bold text-xl shadow-lg border-2 border-blue-400`}>
                {thesis > 0 ? '+' : thesis < 0 ? '−' : '0'}
              </div>
            </div>
            <span className="text-2xl">→</span>
            <div className={`w-24 h-24 ${getStateColor(results.stage3)} rounded-lg flex items-center justify-center font-bold text-3xl shadow-lg ring-4 ring-green-400`}>
              {results.stage3 > 0 ? '+' : results.stage3 < 0 ? '−' : '0'}
            </div>
            <div className="ml-4">
              <div className="text-sm font-semibold text-green-300">Stage 3: Synthesis</div>
              <div className="text-xs text-slate-400">{getStateName(results.stage3)}</div>
            </div>
          </div>
          {showSteps && (
            <div className="bg-slate-900 p-3 rounded text-sm text-slate-300 ml-4">
              Biased Conflict ⊗ Thesis = {getStateLabel(results.stage2)} ⊗ {getStateLabel(thesis)} = {getStateLabel(results.stage3)}
              <br/>
              Final resolution incorporates original thesis with transformed conflict state
            </div>
          )}
        </div>
      </div>

      {/* Results Panel */}
      <div className="bg-gradient-to-r from-green-900/50 to-blue-900/50 p-6 rounded-lg border border-green-700/50 mb-6">
        <h3 className="text-xl font-bold mb-3 text-green-300">Dialectic Resolution</h3>
        <div className="grid grid-cols-2 gap-4">
          <div>
            <div className="text-sm text-slate-400 mb-1">Input States</div>
            <div className="text-sm">
              Thesis: <span className="font-mono text-blue-300">{getStateLabel(thesis)}</span><br/>
              Antithesis: <span className="font-mono text-red-300">{getStateLabel(antithesis)}</span><br/>
              Context: <span className="font-mono text-purple-300">{getStateLabel(context)}</span>
            </div>
          </div>
          <div>
            <div className="text-sm text-slate-400 mb-1">Final Synthesis</div>
            <div className={`inline-block px-4 py-2 rounded-lg ${getStateColor(results.stage3)} font-bold text-lg`}>
              {getStateLabel(results.stage3)}
            </div>
            <div className="text-xs text-slate-300 mt-2">
              {getStateName(results.stage3)}
            </div>
          </div>
        </div>
      </div>

      {/* Control Buttons */}
      <div className="flex gap-3">
        <button
          onClick={reset}
          className="flex items-center gap-2 px-4 py-2 bg-slate-700 hover:bg-slate-600 rounded-lg transition"
        >
          <RotateCcw className="w-4 h-4" />
          Reset to Default
        </button>
      </div>

      {/* Theory Note */}
      <div className="mt-6 p-4 bg-slate-800/50 rounded-lg border border-slate-700">
        <h4 className="font-semibold mb-2 text-sm text-slate-300">Topological Dialectic Logic</h4>
        <p className="text-xs text-slate-400 leading-relaxed">
          This circuit implements Hegelian dialectic using three chained Kauffman gates. The thesis encounters its antithesis (creating conflict), the macro-flux context biases this conflict, and finally the synthesis emerges by reintegrating the original thesis. Unlike binary logic, opposite states annihilate (±1 → 0), same states reinforce (±1 ⊗ ±1 → ±1), and neutral states propagate identity. This creates a topologically protected computation where information persists in the emitted wave during annihilation events.
        </p>
      </div>
    </div>
  );
};

export default TriQbitDialectic;

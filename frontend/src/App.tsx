import { useState } from 'react';
import { analyzeRelease } from './services/api';
import type { ReleaseAnalysis } from './types/analysis'; 
import './App.css';
import ReleaseInput from './components/ReleaseInput';
import RiskLevel from './components/RiskLevel';
import EvidenceSection from './components/EvidenceSection';

function App() {
  const [releaseDescription, setReleaseDescription] = useState('');

  const [analysis, setAnalysis] = useState<ReleaseAnalysis | null>(null);

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState<string | null>(null);

  async function handleAnalyze() {
    if (!releaseDescription.trim()) {
      return;
    }

    try {
      setLoading(true);
      setError(null);

      const result = await analyzeRelease(releaseDescription);

      setAnalysis(result);
    } catch (err) {
      setError(
        err instanceof Error ? err.message : 'Failed to analyze release',
      );
    } finally {
      setLoading(false);
    }
  }

  console.log('Analysis result:', analysis); // Log the analysis result for debugging

  return (
    <div className='app'>
      <header className='app-header'>
        <div className='header-container'>
          <div className='brand'>
            <div className='brand-logo'>R</div>

            <div>
              <h1>ReleaseLens AI</h1>
              <p>AI-powered release risk analysis</p>
            </div>
          </div>

          <span className='ai-badge'>AI + RAG</span>
        </div>
      </header>

      <main className='main-container'>
        <div className='page-intro'>
          <h2>Release Risk Analysis</h2>
          <p>
            Analyze release changes using historical incidents, architecture
            decisions, and engineering evidence.
          </p>
        </div>

        <ReleaseInput
          value={releaseDescription}
          onChange={setReleaseDescription}
          onAnalyze={handleAnalyze}
          loading={loading}
        />

        {analysis && (
          <div className='results'>
            <RiskLevel risk={analysis.risk_level} />

            {/* your AnalysisSection components */}

            <EvidenceSection
              evidence={
                analysis.evidence as unknown as Parameters<
                  typeof EvidenceSection
                >[0]['evidence']
              }
            />
          </div>
        )}
        {
          error && (
            <div className='error-message'>
              <p>Error: {error}</p>
            </div>
          )
        }
      </main>
    </div>
  );
}

export default App;

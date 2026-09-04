interface Evidence {
  document_id: string;
  document_type: string;
  source: string;
  claim: string;
}

interface EvidenceSectionProps {
  evidence: Evidence[];
}

export default function EvidenceSection({ evidence }: EvidenceSectionProps) {
  if (!evidence || evidence.length === 0) {
    return null;
  }

  return (
    <article className='analysis-card evidence-section'>
      <div className='section-title'>
        <span className='section-icon'>🔎</span>

        <div>
          <h3>Evidence</h3>
          <span className='section-subtitle'>
            Retrieved supporting evidence
          </span>
        </div>
      </div>

      <div className='evidence-list'>
        {evidence.map((item, index) => (
          <div className='evidence-card' key={`${item.document_id}-${index}`}>
            <div className='evidence-top'>
              <div className='document-info'>
                <span className='document-icon'>📄</span>

                <div>
                  <strong>{item.document_id}</strong>

                  <span className='document-type'>{item.document_type}</span>
                </div>
              </div>

              <span className='evidence-number'>#{index + 1}</span>
            </div>

            <div className='claim'>
              <span className='claim-label'>Claim</span>
              <p>{item.claim}</p>
            </div>

            <div className='source'>
              <span>Source</span>
              <code>{item.source}</code>
            </div>
          </div>
        ))}
      </div>
    </article>
  );
}

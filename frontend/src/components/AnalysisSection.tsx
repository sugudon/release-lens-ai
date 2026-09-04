interface AnalysisSectionProps {
  title: string;
  content?: string;
  items?: string[];
  icon?: string;
}

export default function AnalysisSection({
  title,
  content,
  items,
  icon = '▸',
}: AnalysisSectionProps) {
  if (!content && (!items || items.length === 0)) {
    return null;
  }

  return (
    <article className='analysis-card'>
      <div className='section-title'>
        <span className='section-icon'>{icon}</span>
        <h3>{title}</h3>
      </div>

      {content && <p className='section-content'>{content}</p>}

      {items && items.length > 0 && (
        <div className='analysis-items'>
          {items.map((item, index) => (
            <div className='analysis-item' key={index}>
              <span className='item-bullet'>✓</span>
              <span>{item}</span>
            </div>
          ))}
        </div>
      )}
    </article>
  );
}

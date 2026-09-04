interface RiskLevelProps {
  risk: string;
}

export default function RiskLevel({ risk }: RiskLevelProps) {
  const normalizedRisk = risk?.toLowerCase() || 'unknown';

  const riskConfig: Record<
    string,
    {
      icon: string;
      description: string;
    }
  > = {
    low: {
      icon: '✓',
      description: 'Low impact release',
    },
    medium: {
      icon: '!',
      description: 'Moderate release risk',
    },
    high: {
      icon: '⚠',
      description: 'High impact release',
    },
    critical: {
      icon: '⚡',
      description: 'Critical release risk',
    },
    unknown: {
      icon: '?',
      description: 'Risk could not be determined',
    },
  };

  const config = riskConfig[normalizedRisk] || riskConfig.unknown;

  return (
    <section className={`risk-card risk-${normalizedRisk}`}>
      <div className='risk-icon'>{config.icon}</div>

      <div className='risk-info'>
        <span className='risk-label'>AI Risk Assessment</span>

        <strong>{risk || 'Unknown'}</strong>

        <span className='risk-description'>{config.description}</span>
      </div>

      <div className='risk-indicator'>
        <span />
        <span />
        <span />
      </div>
    </section>
  );
}

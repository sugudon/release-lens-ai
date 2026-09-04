interface ReleaseInputProps {
  value: string;
  onChange: (value: string) => void;
  onAnalyze: () => void;
  loading?: boolean;
}

export default function ReleaseInput({
  value,
  onChange,
  onAnalyze,
  loading = false,
}: ReleaseInputProps) {
  return (
    <section className='input-card'>
      <div className='input-header'>
        <div className='input-icon'>✦</div>

        <div>
          <h2>Analyze a Release</h2>

          <p>
            Describe your upcoming release and let AI assess its potential risk.
          </p>
        </div>
      </div>

      <label htmlFor='release-description'>Release Description</label>

      <textarea
        id='release-description'
        value={value}
        onChange={event => onChange(event.target.value)}
        placeholder={`Example:

Migrate Payment API from v1 to v2.
Change retry behavior from 3 retries to 5 retries.
The change will be deployed to production next week.
This change only affects the footer text displayed on the website.`}
        rows={9}
        disabled={loading}
      />

      <div className='input-footer'>
        <span className='character-count'>{value.length} characters</span>

        <button
          type='button'
          onClick={onAnalyze}
          disabled={loading || !value.trim()}
        >
          {loading ? (
            <>
              <span className='spinner' />
              Analyzing...
            </>
          ) : (
            <>
              Analyze Release
              <span className='button-arrow'>→</span>
            </>
          )}
        </button>
      </div>
    </section>
  );
}

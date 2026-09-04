export interface ReleaseAnalysis {
  risk_level: string;
  summary: string;
  affected_components: string[];
  historical_incidents: string[];
  architecture_decisions: string[];
  risks: string[];
  testing_recommendations: string[];
  evidence: string[];
  sources: string[];
  uncertainty?: string;
}
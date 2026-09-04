import type { ReleaseAnalysis } from "../types/analysis";

const API_BASE_URL = "http://localhost:8000";

export async function analyzeRelease(
  releaseDescription: string
): Promise<ReleaseAnalysis> {
  const response = await fetch(
    `${API_BASE_URL}/api/releases/analyze`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        release_description: releaseDescription,
      }),
    }
  );

  if (!response.ok) {
    throw new Error(
      `Analysis failed: ${response.status}`
    );
  }

  return response.json();
}
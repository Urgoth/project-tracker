import { apiConfig } from './config'

export class ApiClient {
  constructor(private readonly baseUrl: string) {}

  async getHealth(): Promise<unknown> {
    const response = await fetch(`${this.baseUrl}/health`)

    if (!response.ok) {
      throw new Error(`API request failed with status ${response.status}`)
    }

    return response.json()
  }
}

export const apiClient = new ApiClient(apiConfig.baseUrl)

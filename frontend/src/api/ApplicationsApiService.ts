import { API_URL } from '@/config';
import { Application, ChangeApplicationStatusParams, FetchApplicationsParams } from './models';
import { get, post } from './http';

class ApplicationsApiService {
    public async fetchApplications(params: FetchApplicationsParams) {
        const response = await get<Application[]>(`${API_URL}/api/v1/applications`, {
            params,
        });

        return response;
    }

    public async changeApplicationStatus({
        applicationId,
        ...params
    }: ChangeApplicationStatusParams) {
        await post(`${API_URL}/api/v1/applications/applications/${applicationId}/status`, params);
    }
}

export default new ApplicationsApiService();

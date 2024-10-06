import { API_URL } from '@/config';
import { Application, FetchApplicationsParams } from './models';
import { get } from './http';

class ApplicationsApiService {
    public async fetchApplications(params: FetchApplicationsParams) {
        const response = await get<Application[]>(`${API_URL}/api/v1/applications`, {
            params,
        });

        return response;
    }
}

export default new ApplicationsApiService();

import axios from 'axios';

import { API_URL } from '@/config';
import { Application, FetchApplicationsParams } from './models';

class ApplicationsApiService {
    public async fetchApplications(params: FetchApplicationsParams) {
        const response = await axios.get<Application[]>(`${API_URL}/api/v1/applications`, {
            params,
        });

        return response.data;
    }
}

export default new ApplicationsApiService();

import axios from 'axios';

import { API_URL } from '@/config';
import { AddCandidateToFolderParams, CreateFolderParams, Folder } from './models';

class FoldersApiService {
    public async fetchFolders() {
        const response = await axios.get<Folder[]>(`${API_URL}/api/v1/folders`);

        return response.data;
    }

    public async createFolder({ name }: CreateFolderParams) {
        const response = await axios.post<Folder>(`${API_URL}/api/v1/folders`, { name });

        return response.data;
    }

    public async addCandidateToFolder({ folderId, ...params }: AddCandidateToFolderParams) {
        await axios.post(`${API_URL}/api/v1/folders/${folderId}`, params);
    }
}

export default new FoldersApiService();

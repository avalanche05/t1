import { Route, Routes } from 'react-router-dom';
import { Login } from './pages/Login';
import { RequireAuth } from './auth/RequireAuth';
import { AuthProvider } from './auth/AuthProvider';
import { RequireUnauth } from './auth/RequireUnauth';
import { Dashboard } from './components/Dashboard';
import { Toaster } from './components/ui/toaster';
import { Pages } from './router/constants';
import Home from './pages/Home';
import Applications from './pages/Applications';
import Vacancies from './pages/Vacancies';

function App() {
    return (
        <>
            <Toaster />

            <AuthProvider>
                <Routes>
                    <Route
                        path={`/${Pages.Login}`}
                        element={
                            <RequireUnauth>
                                <Login />
                            </RequireUnauth>
                        }
                    />
                    <Route
                        path={`/${Pages.Home}`}
                        element={
                            <RequireAuth>
                                <Dashboard>
                                    <Home />
                                </Dashboard>
                            </RequireAuth>
                        }
                    />
                    <Route
                        path={`/${Pages.Applications}`}
                        element={
                            // <RequireAuth>
                            <Dashboard>
                                <Applications />
                            </Dashboard>
                            // </RequireAuth>
                        }
                    />
                    <Route
                        path={`/${Pages.Vacancies}`}
                        element={
                            // <RequireAuth>
                            <Dashboard>
                                <Vacancies />
                            </Dashboard>
                            // </RequireAuth>
                        }
                    />
                    <Route
                        path='*'
                        element={
                            <RequireAuth>
                                <Dashboard>
                                    <Home />
                                </Dashboard>
                            </RequireAuth>
                        }
                    />
                </Routes>
            </AuthProvider>
        </>
    );
}

export default App;

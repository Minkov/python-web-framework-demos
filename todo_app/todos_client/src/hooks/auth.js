import {createContext, useCallback, useContext, useEffect, useState} from "react";
import {useServices} from "./services";

const AuthContext = createContext();

const useAuth = () => useContext(AuthContext);

const urls = {
    login: 'http://localhost:8000/api/auth/login/',
    register: 'http://localhost:8000/api/auth/register/',
    logout: 'http://localhost:8000/api/auth/logout/',
};

const AuthProvider = ({children, initialIsLoggedIn}) => {
    const [isLoggedIn, setLoggedIn] = useState(initialIsLoggedIn);
    const {
        httpService,
        storageService,
    } = useServices();

    const login = useCallback(
        async (username, password) => {
            const credentials = {username, password};
            const {token} = await httpService.post(urls.login, credentials);
            storageService.set('token', token);
            setLoggedIn(true);
        },
        [httpService, storageService],
    );

    const register = useCallback(
        async (username, password) => {
            const credentials = {username, password};
            await httpService.post(urls.register, credentials);
        },
        [httpService],
    );

    const logout = useCallback(
        () => {
        },
        [],
    );

    const value = {
        isLoggedIn,
        login,
        register,
        logout,
    };

    return <AuthContext.Provider value={value}>
        {children}
    </AuthContext.Provider>
}

export {
    useAuth,
}

export default AuthProvider;
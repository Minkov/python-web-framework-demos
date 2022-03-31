import {createContext, useContext} from "react";
import HttpService from "../services/http";
import StorageService from "../services/storage";

const ServicesContext = createContext();

const useServices = () => useContext(ServicesContext);

const ServicesProvider = ({children}) => {
    const storageService = new StorageService();
    const httpService = new HttpService(storageService);

    const value = {
        httpService,
        storageService,
    };

    return (
        <ServicesContext.Provider value={value}>
            {children}
        </ServicesContext.Provider>
    );
}

export default ServicesProvider;

export {
    useServices,
};
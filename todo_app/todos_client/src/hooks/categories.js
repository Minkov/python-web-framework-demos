import {createContext, useCallback, useContext, useState} from "react";
import {useServices} from "./services";

const CategoriesContext = createContext();

const useCategories = () => useContext(CategoriesContext);

const CategoriesProvider = ({children}) => {
    const [categories, setCategories] = useState([]);

    const {
        httpService,
    } = useServices();

    const loadCategories = useCallback(
        async () => {
            const categories = await httpService.get('http://localhost:8000/api/todos/categories/');
            setCategories(categories);
        },
        [httpService],
    );

    const value = {
        categories,
        loadCategories,
    };

    return (
        <CategoriesContext.Provider value={value}>
            {children}
        </CategoriesContext.Provider>
    );
}

export default CategoriesProvider;

export {
    useCategories,
};
import {createContext, useCallback, useContext, useEffect, useState} from "react";
import {useServices} from "./services";

const TodosContext = createContext();

const useTodos = () => useContext(TodosContext);

const TodosProvider = ({children}) => {
    const [todos, setTodos] = useState([]);
    const [todoDetails, setTodoDetails] = useState({});
    const [query, setQuery] = useState({});
    const {
        httpService,
    } = useServices();

    const loadTodos = useCallback(async () => {
        const newTodos = await httpService.get("http://localhost:8000/api/todos/", query);
        setTodos(newTodos);
    }, [httpService, query]);

    const loadTodoDetails = useCallback(
        async (id) => {
            const newTodo = await httpService.get(`http://localhost:8000/api/todos/${id}/`);
            setTodoDetails(newTodo);
        },
        [httpService],
    );

    const changeTodoState = useCallback(
        async () => {
            const {id, is_done} = todoDetails;
            const payload = {
                ...todoDetails,
                is_done: !is_done,
            };
            console.log(payload);
            await httpService.put(`http://localhost:8000/api/todos/${id}/`, payload);
            await loadTodoDetails(id);
        },
        [httpService, loadTodoDetails, todoDetails],
    );

    const createTodo = useCallback(
        async (todo) => {
            await httpService.post('http://localhost:8000/api/todos/', todo);
            await loadTodos();
        },
        [httpService, loadTodos],
    );

    const applyFilter = useCallback(
        ({state, category}) => {
            setQuery({state, category});
        },
        [],
    );

    useEffect(
        () => {
            (async () => {
                await loadTodos();
            })();
        },
        [loadTodos],
    )

    const value = {
        todoDetails,
        todos,
        loadTodos,
        loadTodoDetails,
        changeTodoState,
        createTodo,
        applyFilter,
    };

    return <TodosContext.Provider value={value}>
        {children}
    </TodosContext.Provider>
}

export {
    useTodos,
}

export default TodosProvider;
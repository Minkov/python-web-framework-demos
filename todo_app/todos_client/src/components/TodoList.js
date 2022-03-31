import {useTodos} from "../hooks/todos";
import {useCallback, useEffect, useState} from "react";
import styles from './TodoList.module.scss';
import {Box, Button, Grid, Modal, Paper, Stack, Switch} from "@mui/material";
import {useCategories} from "../hooks/categories";

const modalStyle = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 400,
    bgcolor: 'background.paper',
    border: '2px solid #000',
    boxShadow: 24,
    p: 4,
};

const TodoItem = ({todo}) => {
    const {
        todoDetails,
        loadTodoDetails,
        changeTodoState,
    } = useTodos();

    const [open, setOpen] = useState(false);

    const {
        id,
        title,
    } = todo;

    const handleClick = useCallback(
        async () => {
            await loadTodoDetails(id);
            setOpen(true);
        },
        [id, loadTodoDetails],
    );


    const renderModalContent = useCallback(
        () => {
            const {title, description, is_done: isDone} = todoDetails;

            const handleStateChange = async () => {
                await changeTodoState();
            };
            return (
                <Box>
                    <h3>
                        {title}
                    </h3>
                    <p>
                        {description}
                    </p>
                    <Switch defaultChecked={isDone} onChange={() => handleStateChange()}/>
                </Box>
            )
        },
        [changeTodoState, todoDetails],
    );

    return (
        <>
            <Box sx={{
                // borderBottom: '1px solid black',
                // padding: 15,
                marginTop: 5,
                width: 150,
                textAlign: 'center',
            }}>
                <div className={styles.box}>
                    <h3>{title}</h3>
                    <Button
                        variant='text'
                        onClick={() => handleClick()}>Details</Button>
                </div>
            </Box>

            <Modal open={open} onClose={() => setOpen(false)}>
                <Box sx={modalStyle}>
                    {renderModalContent()}
                </Box>
            </Modal>
        </>
    );
}

const TodosList = () => {
    const {
        todos,
        loadTodos,
        applyFilter,
    } = useTodos();

    const [filter, setFilter] = useState({});

    const {
        categories,
        loadCategories,
    } = useCategories();

    const handleChangeCategory = useCallback(
        (id) => {
            setFilter({
                ...filter,
                category: id,
            });
        },
        [filter],
    )

    useEffect(() => {
        (async () => {
            await loadTodos();
        })();
    }, [loadTodos]);

    useEffect(
        () => {
            (async () => {
                await loadCategories();
            })();
        },
        [loadCategories],
    );

    useEffect(
        () => {
            (() => {
                applyFilter(filter);
            })();
        },
        [applyFilter, filter],
    );

    return (
        <div>
            <Stack direction='row'>
                <Button onClick={() => handleChangeCategory('')}>All</Button>
                {
                    categories.map(({name, id}) => (
                        <Button onClick={() => handleChangeCategory(id)}>{name}</Button>
                    ))
                }
            </Stack>
            <Grid container>
                {todos.map(todo => (
                    <Grid item key={todo.id} xs={4}>
                        <TodoItem todo={todo}/>
                    </Grid>
                ))}
            </Grid>
        </div>
    )
};

export default TodosList;
const FetchData = query => {
    const initialState = {
        error: undefined,
        data: undefined
    };

    const fetchReducer = (state, action) => {
        switch (action.type) {
            case "loading":
                return { ...initialState };
            case "fetched":
                return { ...initialState, data: action.payload };
            case "error":
                return { ...initialState, error: action.payload };
            default:
                return state;
        }
    };

    const [state, dispatch] = React.useReducer(fetchReducer, initialState);

    const fetchData = async () => {
        dispatch({ type: "loading" });

        try {
            const response = await fetch(
                `{% url 'imdb:search' %}?query=${query}`
            );
            const data = await response.json();
            dispatch({ type: "fetched", payload: data });
        } catch (error) {
            dispatch({ type: "error", payload: error.message });
        }
    };

    fetchData();

    return state;
};

export default FetchData;

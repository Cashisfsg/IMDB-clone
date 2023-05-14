const initialState = {
    error: undefined,
    data: undefined,
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

const useFetch = (query) => {
    const [state, dispatch] = React.useReducer(fetchReducer, initialState);

    const fetchData = async (query) => {
        dispatch({ type: "loading" });

        console.log(state, query);

        try {
            const response = await fetch(
                `http://localhost:8001/imdb/search?query=${query}`
            );
            const data = await response.json();
            dispatch({ type: "fetched", payload: data?.movies });
        } catch (error) {
            dispatch({ type: "error", payload: error.message });
        }
    };

    React.useEffect(() => {
        fetchData(query);
    }, [query]);

    return state;
};

function useDebounce(value, delay = 500) {
    const [debouncedValue, setDebouncedValue] = React.useState(value);

    React.useEffect(() => {
        const timer = setTimeout(() => setDebouncedValue(value), delay);

        return () => {
            clearTimeout(timer);
        };
    }, [value, delay]);

    return debouncedValue;
}

function SearchList() {
    const [query, setQuery] = React.useState("");

    React.useEffect(() => {
        const inputQuery = document.getElementById("query-field");
        let timer;
        inputQuery.addEventListener("input", (e) => {
            setQuery(e.target.value);
        });
        return () => {
            clearTimeout(timer);
        };
    }, []);

    const debouncedQuery = useDebounce(query);

    const { movies } = useFetch(debouncedQuery);

    console.log("movies", movies);

    return (
        <div>
            {movies &&
                movies.map((movie) => (
                    <li key={movie?.id}>
                        <a href="#">
                            <p className="text-red-500">{movie?.title}</p>
                        </a>
                    </li>
                ))}
        </div>
    );
}

const container = document.getElementById("search-results-container");
const root = ReactDOM.createRoot(container);
root.render(
    <React.StrictMode>
        <SearchList />
    </React.StrictMode>
);

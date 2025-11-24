const fetchItems = async () => {
    try {
        const response = await fetch(`http://127.0.0.1:8000/items/?price=${price}`);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        setItems(data);
    } catch (error) {
        console.error("There was a problem with the fetch operation:", error);
        // Optionally, you could set some state here to display an error message
    }
};

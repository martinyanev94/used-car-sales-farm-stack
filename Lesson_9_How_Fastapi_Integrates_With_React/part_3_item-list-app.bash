npx create-react-app my-app
cd my-app
import React, { useEffect, useState } from 'react';

const ItemList = () => {
    const [items, setItems] = useState([]);

    useEffect(() => {
        const fetchItems = async () => {
            const response = await fetch('http://127.0.0.1:8000/items/');
            const data = await response.json();
            setItems(data);
        };
        fetchItems();
    }, []);

    return (
        <div>
            <h1>Item List</h1>
            <ul>
                {items.map(item => (
                    <li key={item.id}>
                        {item.name}: ${item.price}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ItemList;
import React from 'react';
import ItemList from './ItemList';

function App() {
    return (
        <div className="App">
            <ItemList />
        </div>
    );
}

export default App;
npm start

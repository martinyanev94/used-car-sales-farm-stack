from fastapi import Query

@app.get("/items/")
async def read_items(price: float = Query(None, description="Filter items by price")):
    if price:
        filtered_items = [item for item in items if item['price'] <= price]
        return filtered_items
    return items
import React, { useEffect, useState } from 'react';

const ItemList = () => {
    const [items, setItems] = useState([]);
    const [price, setPrice] = useState('');

    useEffect(() => {
        fetchItems();
    }, []);

    const fetchItems = async () => {
        const response = await fetch(`http://127.0.0.1:8000/items/?price=${price}`);
        const data = await response.json();
        setItems(data);
    };

    const handlePriceChange = (event) => {
        setPrice(event.target.value);
    };

    const handleFilterSubmit = (event) => {
        event.preventDefault();
        fetchItems();
    };

    return (
        <div>
            <h1>Item List</h1>
            <form onSubmit={handleFilterSubmit}>
                <input
                    type="number"
                    value={price}
                    onChange={handlePriceChange}
                    placeholder="Maximum price"
                    min="0"
                />
                <button type="submit">Filter</button>
            </form>
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

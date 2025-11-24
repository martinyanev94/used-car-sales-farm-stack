@app.get("/users/", response_model=List[User])
async def get_users():
    users = list(collection.find({}, {'_id': 0}))  # Hide the MongoDB ObjectId
    return users
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
    const [users, setUsers] = useState([]);
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');

    const fetchUsers = async () => {
        try {
            const response = await axios.get('http://localhost:8000/users/');
            setUsers(response.data);
        } catch (error) {
            console.error("There was an error fetching the users!", error);
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const user = { name, email };

        try {
            await axios.post('http://localhost:8000/users/', user);
            alert("User created!");
            fetchUsers();  // Refresh the user list
        } catch (error) {
            console.error("There was an error creating the user!", error);
        }
    };

    useEffect(() => {
        fetchUsers();
    }, []);

    return (
        <div>
            <h1>Create User</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    placeholder="Name"
                    required
                />
                <input
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="Email"
                    required
                />
                <button type="submit">Submit</button>
            </form>
            <h2>Users List</h2>
            <ul>
                {users.map((user, index) => (
                    <li key={index}>{user.name} - {user.email}</li>
                ))}
            </ul>
        </div>
    );
}

export default App;

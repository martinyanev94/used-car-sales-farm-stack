npx create-react-app farm-stack-frontend
cd farm-stack-frontend
import React, { useEffect, useState } from 'react';

function App() {
    const [users, setUsers] = useState([]);
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');

    const fetchUsers = async () => {
        const response = await fetch('http://127.0.0.1:8000/users/');
        const data = await response.json();
        setUsers(data);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await fetch('http://127.0.0.1:8000/users/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, email }),
        });
        if (response.ok) {
            setName('');
            setEmail('');
            fetchUsers();
        }
    };

    useEffect(() => {
        fetchUsers();
    }, []);

    return (
        <div>
            <h1>User Management</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    required
                />
                <input
                    type="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                />
                <button type="submit">Add User</button>
            </form>
            <h2>Users List</h2>
            <ul>
                {users.map((user) => (
                    <li key={user._id}>{user.name} - {user.email}</li>
                ))}
            </ul>
        </div>
    );
}

export default App;
npm start

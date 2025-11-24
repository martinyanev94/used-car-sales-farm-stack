import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
    const [users, setUsers] = useState([]);
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [loading, setLoading] = useState(true);  // Loading state

    const fetchUsers = async () => {
        setLoading(true);
        try {
            const response = await axios.get('http://localhost:8000/users/');
            setUsers(response.data);
        } catch (error) {
            console.error("There was an error fetching the users!", error);
        } finally {
            setLoading(false);
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

    if (loading) return <div>Loading...</div>;  // Loading message

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
@app.post("/users/", response_model=User)
async def create_user(user: User):
    try:
        user_dict = user.dict()
        collection.insert_one(user_dict)
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to create user due to a database error.")

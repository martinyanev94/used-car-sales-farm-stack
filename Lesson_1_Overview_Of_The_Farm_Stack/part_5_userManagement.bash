npm install axios
import axios from 'axios';

const fetchUsers = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/users/');
        setUsers(response.data);
    } catch (error) {
        console.error('Error fetching users:', error);
    }
};

const handleSubmit = async (e) => {
    e.preventDefault();
    try {
        await axios.post('http://127.0.0.1:8000/users/', { name, email });
        setName('');
        setEmail('');
        fetchUsers();
    } catch (error) {
        console.error('Error adding user:', error);
    }
};

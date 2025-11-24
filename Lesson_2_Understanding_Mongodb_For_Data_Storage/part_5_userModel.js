const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
    name: String,
    email: String,
    posts: [String]
});

const User = mongoose.model('User', userSchema);

// Create a new user
const createUser = async (name, email, posts) => {
    const newUser = new User({ name, email, posts });
    await newUser.save();
}

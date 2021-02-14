import axios from "axios";
const api = "http://127.0.0.1:5000/";
const errors = document.querySelector(".errors");
const loading = document.querySelector(".loading");
const exactMeme = document.querySelector(".exactMeme");
const randomMeme = document.querySelector(".randomMeme");
const results = document.querySelector(".result-container");
results.style.display = "none";
loading.style.display = "none";
errors.textContent = "";

const form = document.querySelector(".form-data");
const meme = document.querySelector(".meme-name");

const searchForMeme = async memeName => {
  loading.style.display = "block";
  errors.textContent = "";
  try {
    const response = await axios.get(`${api}/getSpecificMeme/${memeName}`);
    const response2 =await axios.get(`${api}/getRandomMeme`)
    loading.style.display = "none";
    exactMeme.textContent = response.data;
    randomMeme.textContent = response2.data;
    results.style.display = "block";
  } catch (error) {
    loading.style.display = "none";
    results.style.display = "none";
    errors.textContent = "We have no data for the meme you have requested.";
  }
};

const handleSubmit = async e => {
  e.preventDefault();
  searchForMeme(meme.value);
  console.log(meme.value);
};

form.addEventListener("submit", e => handleSubmit(e));

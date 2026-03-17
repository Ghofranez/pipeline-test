// src/api.js
const API_URL = "http://localhost:8000";  // l'URL de ton backend en dev

export async function getData(endpoint) {
  try {
    const response = await fetch(`${API_URL}/${endpoint}`);
    if (!response.ok) {
      throw new Error(`Erreur API: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error(error);
    return null;
  }
}
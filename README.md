# esme-web-services-TP

Modifications
---

# 📚 API Endpoints

---

## 🔹 Emprunter un livre  
`POST /books/<book_id>/borrow`  
Content-Type: `application/json`  
Permet à un étudiant d'emprunter un livre s’il n’est pas déjà emprunté.

```json
{
  "student_id": 1
}
```

🛈 Si le livre est déjà emprunté (non rendu), l’API retourne une erreur 400.

---

## 🔹 Rendre un livre  
`POST /books/<book_id>/return`  
Content-Type: `application/json`  
Permet à un étudiant de rendre un livre qu’il a emprunté.

```json
{
  "student_id": 1
}
```

---

## 👨‍🎓 Students

### 🔹 Récupérer tous les étudiants  
`GET /students`

---

### 🔹 Récupérer un étudiant spécifique  
`GET /students/<student_id>`

---

### 🔹 Ajouter un étudiant  
`POST /students`  
Content-Type: `application/json`

```json
{
  "first_name": "Marie",
  "last_name": "Dupont",
  "email": "marie.dupont@email.com",
  "birth_date": "2000-01-01"
}
```

---

### 🔹 Mettre à jour un étudiant  
`PUT /students/<student_id>`  
Content-Type: `application/json`

```json
{
  "first_name": "Maria"
}
```

---

### 🔹 Supprimer un étudiant  
`DELETE /students/<student_id>`

# esme-web-services-TP

Modifications des Endpoints
---

# 📚 Books


## 🔹 Emprunter un livre  
```
POST /books/<book_id>/borrow  
Content-Type: application/json

json
{
  "student_id": 1
}
```

---

## 🔹 Rendre un livre  
```
POST /books/<book_id>/return
  
Content-Type: application/json 

json
{
  "student_id": 1
}
```

---

## 👨‍🎓 Students

### 🔹 Récupérer tous les étudiants  
```
GET /students
```

---

### 🔹 Récupérer un étudiant spécifique  
```
GET /students/<student_id>
```

---

### 🔹 Ajouter un étudiant  
```
POST /students  
Content-Type: application/json

json
{
  "first_name": "Marie",
  "last_name": "Dupont",
  "email": "marie.dupont@email.com",
  "birth_date": "2000-01-01"
}
```

---

### 🔹 Mettre à jour un étudiant  
```
PUT /students/<student_id> 
Content-Type: application/json

json
{
  "first_name": "Maria"
}
```

---

### 🔹 Supprimer un étudiant  
```
DELETE /students/<student_id>
```

---
## Modifications de app.py

```
from routes.students import students_bp
app.register_blueprint(students_bp)
```



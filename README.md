
# 🔐 Django Login & Signup System

This project showcases a custom login and signup system in Django, built using Django's built-in authentication system, but extended and styled to fit real-world scenarios. It uses a **custom user model** with email-based authentication and personalized form validation messages.

---

## 📘 What I Learned

Throughout this project, I gained a deeper understanding of Django's authentication system, including:

- Creating a **custom user model** using `AbstractBaseUser` and `PermissionsMixin`.
- Managing users through a **custom user manager** (`BaseUserManager`) with `create_user()` and `create_superuser()` functions.
- Using **email instead of username** for authentication.
- Building a **signup form** that collects:
  - First Name
  - Last Name
  - Email
  - Password
- Creating a **login form** that requires:
  - Email
  - Password
- Handling form validation and password confirmation.
- Displaying field-specific error messages.
- Redirecting users to the correct pages after login/signup.
- Linking templates and pages to one another.
- Extending all templates from a single `base.html` for consistent layout and reusability.

---

## 🧱 Custom Template Flow

All templates extend from a common base for consistency and DRY design:

```
base.html
├── signup.html
├── login.html
└── home.html
```

- `signup.html` → user enters first name, last name, email, and password.
- `login.html` → user logs in with email and password.
- Both pages extend `base.html` and include CSRF protection and error handling.
- Pages are linked, so users can switch between login and signup easily.

---

## 🚧 Challenges Faced During the Project

### 1. **Custom User Model Complexity**
- Learning how `AbstractBaseUser` and `PermissionsMixin` work together.
- Setting up required fields like `first_name`, `last_name`, and `email` correctly.
- Understanding `USERNAME_FIELD` and `REQUIRED_FIELDS` configuration.

### 2. **Default Values and IntegrityError**
- Faced errors like:
  ```
  IntegrityError: null value in column "date_joined"
  ```
- Learned that using `default=timezone.now` is essential when a field (like `date_joined`) is `NOT NULL`.

### 3. **Custom User Manager Pitfalls**
- Misused `extra_fields.is_default()` instead of `extra_fields.setdefault()`.
- Solved it by properly setting `is_staff` and `is_superuser` in the manager method.

### 4. **Form Error Placement**
- Initially struggled with placing validation messages right beneath each field.
- Eventually used Django template tags to iterate over each field’s `.errors` properly.

### 5. **Template Inheritance and Navigation**
- Learned how to properly link pages using `{% url %}` inside templates.
- Ensured all templates inherit from `base.html` and maintain clean structure.

---

## ▶️ How to Run This Project

Anticipate

## 👨‍💻 Built By

**Gaji Yaqub Ayomikun**  
Twitter/X: [@codewithgaji](https://twitter.com/codewithgaji)  
Student of Computer Science, Lagos State University  
Passionate about backend development and building real-world Django applications

---

## ✅ Conclusion

This project helped me understand Django's powerful authentication system, especially with custom user models. Although there were challenges like understanding abstract base classes and field constraints, I now feel confident in:

- Building flexible login/signup systems
- Managing custom user logic
- Designing clean and user-friendly authentication templates

I'm excited to build more projects that involve secure user management and contribute more to open-source Django solutions!

# 🎭 AutomationExercise E2E Playwright Python Framework

Framework profesional de automatización de pruebas UI y API, desarrollado con Python, Pytest y Playwright para la aplicación de comercio electrónico [AutomationExercise](https://www.automationexercise.com/).

---

## 📌 Sobre el proyecto

Este proyecto es un framework profesional de automatización de pruebas diseñado para validar flujos críticos de un comercio electrónico en Automation Exercise. 

La solución combina automatización de interfaces de usuario (UI), pruebas de API, pruebas basadas en datos (Data-Driven Testing), ejecución multiplataforma en distintos navegadores, captura de evidencias ante fallos, generación de reportes e integración con procesos de Integración Continua y Entrega Continua (CI/CD).

Su principal objetivo es demostrar buenas prácticas de Automatización QA escalables y mantenibles, utilizando Python, Pytest y Playwright como tecnologías base.

---

## 🛠️ Tecnologías utilizadas

- Python
- Playwright
- Pytest
- Requests
- pytest-html
- GitHub Actions
- JSON
- Page Object Model

---

## ✅ Funcionalidades probadas 

- User Registration
- Login / Logout
- Product Catalog
- Product Search
- Product Details
- Categories
- Brands
- Shopping Cart
- Checkout
- Payment
- Order Confirmation
- Invoice Download
- API + UI Integration

---

## 🏗️ Arquitectura del Framework

Este framework sigue el patrón de diseño Page Object Model (POM), lo que permite separar la lógica de las pruebas de la lógica de interacción con la interfaz de usuario.

```text
Tests
  |
  v
Page Objects
  |
  v
Playwright
  |
  v
Automation Exercise

Se incluyen capas adicionales para gestionar la comunicación con APIs, los datos de prueba y las utilidades compartidas, facilitando la reutilización de código y el mantenimiento del framework.

Tests
  |
  +---- UI --------> Page Objects ------> Playwright
  |
  +---- API -------> Services ----------> Requests
  |
  +---- Data ------> JSON / Test Data
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

  
Esto ayuda muchísimo a entender el diseño.

---

```markdown
## 📂 Estructura del Proyecto 

```text
.
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── api/
│   ├── api_client.py
│   ├── product_service.py
│   └── user_service.py
│
├── config/
│   └── settings.py
│
├── pages/
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── login_page.py
│   ├── payment_page.py
│   ├── products_page.py
│   ├── account_information_page.py
│   ├── account_page.py
│   ├── base_page.py
│   ├── order_confirmation_page.py
│   ├── product_details_page.py
│   └── signup_page.py
│
├── test_data/
│   ├── users.py
│   ├── payment.py
│   ├── checkout_data.json
│   ├── login_cases.json
│   ├── products.json
│
├── tests/
│   ├── authentication/
│   ├── products/
│   ├── cart/
│   ├── checkout/
│   ├── api_ui/
│   └── e2e/
│
├── utils/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
├── .gitattributes
└── README.md

---

```markdown
## 🎯 Estrategia de Pruebas

El framework organiza las pruebas automatizadas mediante el uso de marcadores (markers) de Pytest.

| Suite | Purpose |
|---|---|
| Smoke | Pruebas críticas del flujo principal de usuario |
| Regression | Suite completa de pruebas de regresión |
| E2E | Flujos de usuario de extremo a extremo (End-to-End) |
| API_UI | Escenarios de integración entre API e interfaz de usuario |
| Critical | Escenarios de prueba de alta prioridad |
| Authentication | Pruebas de autenticación y gestión de usuarios |
| Cart | Pruebas del carrito de compras |
| Checkout | Pruebas de checkout y procesamiento de pagos |
| Products | Pruebas del catálogo y gestión de productos |

Las pruebas están diseñadas para ser independientes y ejecutarse de forma aislada, garantizando su confiabilidad, mantenibilidad y reutilización.

---

## 🔥 Flujo E2E Crítico

```text
Login
  ↓
Products
  ↓
Product Details
  ↓
Add to Cart
  ↓
Cart
  ↓
Checkout
  ↓
Payment
  ↓
Place Order
  ↓
Order Confirmation

---

## ▶️ Instalación

### Prerequisitos

- Python 3.12+
- Git

Clonar:

```bash
git clone <https://github.com/Masuelm04/AutomationExercise-E2E-Playwright-Framework.git>
cd <AutomationExercise-E2E-Playwright-Framework>


Crear entorno virtual:

```markdown
```bash
python -m venv .venv


En Windows PowerShell:

```markdown
```powershell
.venv\Scripts\Activate.ps1


Instalar dependencias:

```markdown
```bash
pip install -r requirements.txt


Instalar browsers:

```markdown
```bash
playwright install

## 🧪 Ejecución de Pruebas

Suite completa:

```markdown
```bash
pytest


Smoke:

```markdown
```bash
pytest -m smoke


Regression:

```markdown
```bash
pytest -m regression


E2E:

```markdown
```bash
pytest -m e2e


---


```markdown
## 🌐 Pruebas Cross-Browser 

El framework soporta Chromium, Firefox y WebKit.

### Chromium

```bash
pytest --browser chromium

### Firefox

```bash
pytest --browser firefox

### WebKit

```bash
pytest --browser webkit

## 📊 Data-Driven Testing

El framework utiliza la parametrización de Pytest y datos externos en formato JSON para ejecutar un mismo comportamiento con múltiples conjuntos de datos.

### Casos de uso
- 🔐 Escenarios de autenticación
- 🔎 Búsqueda de productos
- 🛒 Datos de checkout
- 💳 Flujos de compra

## 🎭 Funcionalidades Avanzadas de Playwright

- File Download
- Trace Viewer
- Screenshots on Failure

## 📊 Reportes y Evidencias

La ejecución de las pruebas genera un reporte HTML mediante **pytest-html**.

Cuando una prueba falla, el framework captura automáticamente evidencia para facilitar el análisis y la depuración del problema:

- 📸 Captura de pantalla de página completa (*Full-page Screenshot*)
- 🔍 Traza de ejecución de Playwright (*Playwright Trace*)

```text
Ejecución de Prueba
      |
      +---- HTML Report
      |
      +---- Failure
                |
                +---- Screenshot
                |
                +---- Playwright Trace

```markdown
Los reportes generados y las evidencias recopiladas se excluyen del control de versiones (*source control*) y se publican como artefactos (*artifacts*) del proceso de Integración Continua (CI). Esto permite acceder y analizar los resultados de las ejecuciones sin almacenar archivos temporales o generados automáticamente dentro del repositorio.

## CI/CD

GitHub Actions ejecuta automáticamente la suite de pruebas **Smoke** en los siguientes escenarios:
 
- 🚀 Cada vez que se realiza un **push** a la rama `main`.
- 🔄 Cuando se crea o actualiza un **Pull Request** dirigido a la rama `main`.
- ▶️ Mediante la ejecución manual del workflow cuando sea necesario.

La canalización de CI utiliza una matriz de navegadores para ejecutar las pruebas en:
 
- 🌐 Chromium
- 🦊 Firefox

Push / Pull Request
        ↓
GitHub Actions
        ↓
Configurar Python
        ↓
Instalar Dependencias
        ↓
Matriz de Navegadores
   ┌────────┼────────┐
   ↓                 ↓
Chromium         Firefox
   └────────┼────────┘
            ↓
        ↓
Ejecutar Pruebas Smoke
        ↓
Generar Reportes HTML
        ↓
Subir Reportes y Evidencias
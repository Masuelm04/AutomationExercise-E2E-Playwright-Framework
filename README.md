# 🎭 AutomationExercise E2E Playwright Python Framework

Framework profesional de automatización de pruebas UI y API desarrollado con **Python, Pytest y Playwright** para la aplicación de comercio electrónico **Automation Exercise**.

🔗 https://www.automationexercise.com/

---

# 📌 Sobre el Proyecto

Este proyecto es un framework profesional de automatización de pruebas diseñado para validar flujos críticos de comercio electrónico en Automation Exercise.

La solución combina:

- Automatización de interfaces de usuario (UI)
- Pruebas API
- Data-Driven Testing
- Ejecución Cross-Browser
- Captura automática de evidencias
- Generación de reportes
- Integración CI/CD mediante GitHub Actions

Su principal objetivo es demostrar buenas prácticas de automatización QA escalables y mantenibles utilizando Python, Pytest y Playwright.

---

# 🛠️ Tecnologías Utilizadas

- Python
- Playwright
- Pytest
- Requests
- pytest-html
- GitHub Actions
- JSON
- Page Object Model (POM)

---

# ✅ Funcionalidades Probadas

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

# 🏗️ Arquitectura del Framework

Este framework sigue el patrón **Page Object Model (POM)** para separar la lógica de negocio de la lógica de interacción con la interfaz.

## Arquitectura General

```text
Tests
  │
  ▼
Page Objects
  │
  ▼
Playwright
  │
  ▼
Automation Exercise
```

## Capas del Framework

```text
Tests
  │
  ├── UI ──────► Page Objects ──────► Playwright
  │
  ├── API ─────► Services ──────────► Requests
  │
  └── Data ────► JSON / Test Data
```

Se incluyen capas adicionales para la comunicación con APIs, gestión de datos de prueba y utilidades compartidas, facilitando la reutilización y el mantenimiento del código.

---

# 📂 Estructura del Proyecto

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
│   └── products.json
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
```

---

# 🎯 Estrategia de Pruebas

El framework organiza las pruebas automatizadas mediante **Pytest Markers**.

| Marker | Descripción |
|----------|-------------|
| smoke | Pruebas críticas del flujo principal |
| regression | Suite completa de regresión |
| e2e | Flujos End-to-End |
| api_ui | Integración entre API y UI |
| critical | Escenarios de alta prioridad |
| authentication | Gestión de usuarios y autenticación |
| cart | Carrito de compras |
| checkout | Flujo de checkout y pagos |
| products | Catálogo y gestión de productos |

Las pruebas están diseñadas para ejecutarse de forma aislada, garantizando independencia, mantenibilidad y reutilización.

---

# 🔥 Flujo E2E Crítico

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
```

---

# ▶️ Instalación

## Prerequisitos

- Python 3.12+
- Git

## Clonar repositorio

```bash
git clone https://github.com/Masuelm04/AutomationExercise-E2E-Playwright-Framework.git

cd AutomationExercise-E2E-Playwright-Framework
```

## Crear entorno virtual

```bash
python -m venv .venv
```

## Activar entorno virtual

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

## Instalar navegadores

```bash
playwright install
```

---

# 🧪 Ejecución de Pruebas

## Suite completa

```bash
pytest
```

## Smoke

```bash
pytest -m smoke
```

## Regression

```bash
pytest -m regression
```

## E2E

```bash
pytest -m e2e
```

---

# 🌐 Pruebas Cross-Browser

El framework soporta:

- 🌐 Chromium
- 🦊 Firefox
- 🧭 WebKit

## Chromium

```bash
pytest --browser chromium
```

## Firefox

```bash
pytest --browser firefox
```

## WebKit

```bash
pytest --browser webkit
```

---

# 📊 Data-Driven Testing

El framework utiliza parametrización de Pytest y archivos JSON externos para ejecutar el mismo comportamiento con distintos conjuntos de datos.

## Casos de Uso

- 🔐 Escenarios de autenticación
- 🔎 Búsqueda de productos
- 🛒 Datos de checkout
- 💳 Flujos de compra

---

# 🔗 Integración API + UI

El proyecto combina operaciones de backend mediante API con validaciones realizadas desde la interfaz de usuario, permitiendo verificar la consistencia de los datos a través de múltiples capas de la aplicación.

Ejemplos:

- Crear o consultar información vía API.
- Validar los datos mostrados en la interfaz.
- Comparar respuestas API con elementos UI.
- Reducir dependencias de preparación manual de datos.

---

# 🎭 Funcionalidades Avanzadas de Playwright

- 📥 File Download
- 🔍 Trace Viewer
- 📸 Screenshots on Failure

---

# 📊 Reportes y Evidencias

La ejecución de pruebas genera reportes HTML mediante **pytest-html**.

Cuando una prueba falla, el framework captura automáticamente:

- 📸 Captura de pantalla de página completa
- 🔍 Playwright Trace

```text
Ejecución de Prueba
      │
      ├── HTML Report
      │
      └── Failure
             │
             ├── Screenshot
             │
             └── Playwright Trace
```

Los reportes y evidencias generados se excluyen del control de versiones y se publican como artefactos del pipeline de Integración Continua.

---

# 🚀 CI/CD

GitHub Actions ejecuta automáticamente la suite **Smoke** en los siguientes escenarios:

- 🚀 Push a `main`
- 🔄 Pull Request hacia `main`
- ▶️ Ejecución manual del workflow

La canalización ejecuta pruebas sobre una matriz de navegadores:

- 🌐 Chromium
- 🦊 Firefox

```text
Push / Pull Request
         │
         ▼
GitHub Actions
         │
         ▼
Configurar Python
         │
         ▼
Instalar Dependencias
         │
         ▼
Matriz de Navegadores
   ┌────────┴────────┐
   ▼                 ▼
Chromium         Firefox
   └────────┬────────┘
            ▼
 Ejecutar Smoke Tests
            ▼
 Generar HTML Reports
            ▼
 Subir Evidencias
```

---
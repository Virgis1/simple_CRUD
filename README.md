**Simple CRUD Project**

**Description**

  This project is a FastAPI application that provides CRUD (Create, Read, Update, Delete) operations for managing items. It includes endpoints for creating, reading, updating, and deleting items.

**Getting Started**

  * Prerequisites
  * Python 3.x
  * FastAPI
  * Pydantic

**Installation**

  pip install fastapi uvicorn

**Usage**

  uvicorn main:app --reload

**Endpoints**

  * POST /items/: Create a new item.
  * GET /items/{name}: Read an item by name.
  * PUT /items/{name}: Update an existing item.
  * DELETE /items/{name}: Delete an item by name.
  * GET /items/: Get all items.

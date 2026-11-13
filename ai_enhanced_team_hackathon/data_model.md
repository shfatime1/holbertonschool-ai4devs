
# Data Model – FridgeMind

## Overview

FridgeMind uses a simple data model to manage users, ingredients, and AI-generated recipes.

The MVP includes four main entities:

1. User
2. Ingredient
3. Recipe
4. RecipeIngredient

## 1. User Entity

Stores basic information about application users.

| Field | Type | Description |
|---|---|---|
| id | Integer | Unique user identifier |
| name | String | User's name |
| email | String | User's email address |
| created_at | DateTime | Account creation date |

**Relationships:**
- One user can have many ingredients.
- One user can save many recipes.

## 2. Ingredient Entity

Stores information about food products in a user's virtual fridge.

| Field | Type | Description |
|---|---|---|
| id | Integer | Unique ingredient identifier |
| user_id | Integer | Reference to the owner |
| name | String | Ingredient name |
| quantity | Decimal | Available quantity |
| unit | String | Measurement unit (kg, g, pieces, etc.) |
| expiration_date | Date | Expiration date |
| created_at | DateTime | Date the ingredient was added |

**Relationships:**
- Each ingredient belongs to one user.
- A user can have multiple ingredients.

## 3. Recipe Entity

Stores AI-generated or saved recipe information.

| Field | Type | Description |
|---|---|---|
| id | Integer | Unique recipe identifier |
| user_id | Integer | Reference to the user |
| title | String | Recipe name |
| description | Text | Short recipe description |
| instructions | Text | Preparation steps |
| created_at | DateTime | Recipe creation date |

**Relationships:**
- Each recipe belongs to one user.
- A recipe can contain multiple ingredients through RecipeIngredient.

## 4. RecipeIngredient Entity

Connects recipes with their required ingredients.

| Field | Type | Description |
|---|---|---|
| id | Integer | Unique record identifier |
| recipe_id | Integer | Reference to a recipe |
| ingredient_id | Integer | Reference to an ingredient |
| quantity_required | Decimal | Required quantity |
| unit | String | Measurement unit |

**Relationships:**
- Each record connects one recipe with one ingredient.
- A recipe can have multiple ingredient records.
- An ingredient can be used in multiple recipes.

## Entity Relationships

- User (1) → (Many) Ingredient
- User (1) → (Many) Recipe
- Recipe (1) → (Many) RecipeIngredient
- Ingredient (1) → (Many) RecipeIngredient

## Data Validation Rules

- User email must be unique.
- Ingredient name cannot be empty.
- Ingredient quantity must be greater than zero.
- Expiration date must be a valid date.
- Recipe title cannot be empty.
- RecipeIngredient must reference existing recipe and ingredient records.

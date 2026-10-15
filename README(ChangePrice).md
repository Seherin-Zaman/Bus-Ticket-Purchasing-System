# Branch Name
- Change Price

## Python File Name
- ChangePrice.py

## CSV File Name
- mobile_products.csv

## Actor
- Admin

## Preconditions
- Admin must be logged in to the system.
- mobile_products.csv may or may not exist.
- The CSV file may contain one or more top-up products.

## Class
- ChangePriceManager

## Methods
  - ### __init__()
  -Initializes the ChangePriceManager class.
- ### clear()
  - Clears the terminal screen.
  - Compatible with Windows, macOS, and Linux.
- ### pause()
  - Pauses execution until the admin presses Enter.
- #### ChangePrice()
  - Displays available top-up products.
  - alidates Topup ID input.
  - Displays current price information.
  - Accepts and validates a new price.
  - Confirms admin action before saving changes.
  - Updates the CSV file with the new price.

## Responsibility
- This class allows the Admin to change the price of an existing mobile top-up product by updating the price stored in the mobile_products.csv file.

## Main Flow
- Admin selects “Change Topup Price” from the admin menu.
- System displays a heading for price modification.
- System checks whether mobile_products.csv exists.
- If the file exists and contains data:
   - Available top-up products are displayed (ID, title, price).
   - Admin enters a valid Topup ID.
   - System displays the current price of the selected top-up.
   - Admin enters a new valid price in pence.
   - Admin confirms the change.
   - System updates the price and saves it to the CSV file.
- Admin is returned to the admin menu.

## Postconditions
- The selected top-up price is updated successfully OR
- No changes are made if the admin cancels.
- Admin is returned to the admin menu.

## Alternative Flow
- If file does not exist
   - System displays: “File not found!”
- Admin is returned to the admin menu.
- If File exists but contains no products
   - System displays: “No products to update.”
- Admin is returned to the admin menu.

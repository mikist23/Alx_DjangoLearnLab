## Permissions and Groups in bookshelf

### Custom Permissions
The `Article` model defines the following permissions:
- `can_view`: Can view articles.
- `can_create`: Can create articles.
- `can_edit`: Can edit articles.
- `can_delete`: Can delete articles.

### Groups
- **Viewers**: Has `can_view` permission.
- **Editors**: Has `can_view`, `can_create`, `can_edit` permissions.
- **Admins**: Has all permissions.
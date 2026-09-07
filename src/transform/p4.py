requested_roles = ["guest", "developer", "guest", "admin", "developer", "guest"] 
required_admin_roles = {"admin", "security_officer", "audit_manager"}


requested_roles_set = set(requested_roles)
print(f"Уникальные запрошенные роли: {requested_roles_set}")

roles_intersect = requested_roles_set & required_admin_roles
print(f"Общие административные роли: {roles_intersect}")

missing_roles = required_admin_roles - requested_roles_set
print(f"Недостающие административные роли: {missing_roles}")

security_officer_role_in_required = "security_officer" in requested_roles_set
print(f"Наличие роли security_officer в запросе: {security_officer_role_in_required}")

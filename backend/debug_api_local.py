from app import create_app
from flask import g
from app.routes.audit_routes import get_audit_logs

app = create_app()

class MockUser:
    Id = 1
    RolId = 1
    def has_permission(self, p): return True

with app.test_request_context('/api/audit/logs?page=1&per_page=10'):
    # Mock user
    g.current_user = MockUser()
    
    try:
        # Call the view function directly. 
        # Note: The view is decorated. accessing the original function might be needed if decorators interfere,
        # but here we want to test the full chain if possible, or at least the logic.
        # Since get_audit_logs is decorated with @token_required, calling it directly requires passing arguments 
        # that the decorator passes? No, the decorator calls the function.
        # But wait, `get_audit_logs` definition is `def get_audit_logs(current_user):`.
        # So we must pass current_user.
        
        response, status = get_audit_logs(g.current_user)
        print(f"Status: {status}")
        print(f"Data: {response.json}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

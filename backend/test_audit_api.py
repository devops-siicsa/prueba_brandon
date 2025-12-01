from app import create_app
from app.utils.decorators import token_required
from flask import g

app = create_app()

# Mocking a request context
with app.test_request_context('/api/audit/logs'):
    # Mocking a user for token_required (though we are calling the function directly if we could, 
    # but better to use the test client)
    pass

client = app.test_client()

# We need a valid token or to bypass auth. 
# For quick testing of the 500 error logic inside the route, let's try to invoke the route function directly 
# if we can import it, or just use the client and expect 401 if no token.
# But we want to trigger the NameError.

# Let's try to authenticate first or mock the auth.
# Actually, the quickest way is to inspect the file again and just fix it because the error is obvious.
# But to follow protocol, I will try to trigger it.

# I'll create a script that imports the blueprint function and calls it with a mock request.
try:
    from app.routes.audit_routes import get_audit_logs
    print("Function imported.")
    
    # Mock g.current_user
    class User:
        Id = 1
        RolId = 1
        def has_permission(self, p): return True
    
    with app.test_request_context('/api/audit/logs?page=1'):
        g.current_user = User()
        # We need to bypass the decorators if we call directly, 
        # but the decorators are wrappers. The original function is wrapped.
        # Calling get_audit_logs(current_user) might work if we pass the arg.
        
        try:
            response = get_audit_logs(g.current_user)
            print("Response:", response)
        except Exception as e:
            print(f"Caught expected error: {e}")
            import traceback
            traceback.print_exc()

except Exception as e:
    print(f"Setup error: {e}")

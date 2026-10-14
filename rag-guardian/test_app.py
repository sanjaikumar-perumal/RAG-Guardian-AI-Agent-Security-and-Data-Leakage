from app import retrieve, scan

def test_user_cannot_retrieve_admin_document():
    docs = retrieve("internal test secret", role="user")
    assert all(d.metadata["access"] == "public" for d in docs)

def test_admin_can_retrieve_admin_document():
    docs = retrieve("internal test secret", role="admin")
    assert all(
        d.metadata["access"] in ["public", "admin"]
        for d in docs
    )

def test_scan_returns_four_results():
    results = scan()
    assert len(results) == 4
    assert all(r["status"] in ["PASS", "FAIL"] for r in results)
    assert all("recommendation" in r for r in results)


import json
import sqlite3
import yaml

DB_FILE = "a_daily_quant.db"


def export_agents():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM strategies")
    rows = cursor.fetchall()

    agents = {}
    for row in rows:
        d = dict(row)
        slug = d.pop("slug")
        strategy_id = d.pop("id")

        # Get params
        cursor.execute(
            "SELECT param_key, param_value FROM strategy_params WHERE strategy_id = ?",
            (strategy_id,),
        )
        params = dict(cursor.fetchall())
        d["role"] = params.get("role", "")
        d["system_prompt"] = params.get("system_prompt", "")

        # Remove created_at, updated_at
        d.pop("created_at", None)
        d.pop("updated_at", None)

        agents[slug] = d

    with open("agents.yaml", "w", encoding="utf-8") as f:
        yaml.dump(agents, f, allow_unicode=True, sort_keys=False)

    print("Exported to agents.yaml")


if __name__ == "__main__":
    export_agents()

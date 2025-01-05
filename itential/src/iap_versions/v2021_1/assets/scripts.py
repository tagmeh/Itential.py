from pathlib import Path


class Scripts:
    def __init__(self, parent: "Itential"):
        self.parent = parent

    def import_repo(self, repo_path: str | Path, path_to_assets: str = "resources/itential/"):
        """
        Given a repository path? find all the assets and follow the Itential instance process for importing each asset type.
        """
        if isinstance(repo_path, str):
            repo_path = Path(repo_path)

        # Validate the repository path
        if not repo_path.exists():
            raise FileNotFoundError(f"Path {repo_path} does not exist.")

        if not repo_path.is_dir():
            raise NotADirectoryError(f"Path {repo_path} is not a directory.")

        asset_path = repo_path.joinpath(path_to_assets)
        # Validate the asset path
        if not asset_path.exists():
            raise FileNotFoundError(f"Path {asset_path} does not exist.")

        if not asset_path.is_dir():
            raise NotADirectoryError(f"Path {asset_path} is not a directory.")

        # Collect workflow assets
        workflow_assets = list(asset_path.glob("workflows/**/*.json"))
        print(len(workflow_assets))

        # Follow repo path
        # Collect the assets, keeping them in their own groupings (workflows in an array of workflows)
        # For each type of asset, call the appropriate itential instance methods
        # Itential methods should give some sort of positive response/receipt to output to the user.
        ...


def scan_for_disallowed_names():
    """
    WIP
    Scan the server for assets with disallowed naming schemes.
    Things that may be disallowed: Spaces, slashes, parenthesis, symbols.
    """


if __name__ == "__main__":
    repo_path = Path(r"\\wsl$\Debian\home\ac08997\IAP-Docker\apps_and_adapters\v2021.1\ctl\app-oaas")
    import_repo(repo_path)

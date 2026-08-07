{
  description = "simple python devshell flake for data structures and algorithms / leetcode prep in python!";
  inputs.nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in {
      devShells.${system}.default = pkgs.mkShell {
        buildInputs = [
          pkgs.uv

          pkgs.python313
          (pkgs.python313.withPackages (ps: [
            ps.pytest
          ]))
        ];

        shellHook = ''
          echo "python: $(python --version)"
          echo "uv: $(uv --version)"
        '';
      };
    };
}

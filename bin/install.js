#!/usr/bin/env node

const fs = require("fs");
const os = require("os");
const path = require("path");

const SKILL_NAME = "oprp-prompt-optimizer";
const PACKAGE_ROOT = path.resolve(__dirname, "..");
const ENTRIES = [
  "SKILL.md",
  "README.md",
  "agents",
  "examples",
  "references",
  "scripts",
  "templates",
  "tests",
];

function usage() {
  return [
    "Install 工程化提示词优化 into Codex skills.",
    "",
    "Usage:",
    "  npx github:FlaxXTT/engineering-prompt-optimizer-skill",
    "  engineering-prompt-optimizer-skill [--target <dir>] [--no-backup]",
    "",
    "Options:",
    "  --target <dir>  Install to a custom skill directory.",
    "  --no-backup    Replace the target without creating a timestamped backup.",
    "  --help         Show this help message.",
  ].join("\n");
}

function parseArgs(argv) {
  const args = {
    target: path.join(os.homedir(), ".codex", "skills", SKILL_NAME),
    backup: true,
  };

  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === "--help" || arg === "-h") {
      console.log(usage());
      process.exit(0);
    }
    if (arg === "--target") {
      const value = argv[i + 1];
      if (!value) {
        throw new Error("--target requires a directory path.");
      }
      args.target = path.resolve(value);
      i += 1;
      continue;
    }
    if (arg === "--no-backup") {
      args.backup = false;
      continue;
    }
    throw new Error(`Unknown option: ${arg}`);
  }

  return args;
}

function copyRecursive(source, destination) {
  const stat = fs.statSync(source);
  if (stat.isDirectory()) {
    fs.mkdirSync(destination, { recursive: true });
    for (const child of fs.readdirSync(source)) {
      copyRecursive(path.join(source, child), path.join(destination, child));
    }
    return;
  }
  fs.copyFileSync(source, destination);
}

function assertPackageComplete() {
  const missing = ENTRIES.filter((entry) => !fs.existsSync(path.join(PACKAGE_ROOT, entry)));
  if (missing.length > 0) {
    throw new Error(`Package is incomplete. Missing: ${missing.join(", ")}`);
  }
}

function installSkill(target, backup) {
  assertPackageComplete();

  const parent = path.dirname(target);
  fs.mkdirSync(parent, { recursive: true });

  if (fs.existsSync(target)) {
    if (backup) {
      const stamp = new Date().toISOString().replace(/[:.]/g, "-");
      const backupTarget = `${target}.backup-${stamp}`;
      fs.renameSync(target, backupTarget);
      console.log(`Existing skill backed up to: ${backupTarget}`);
    } else {
      fs.rmSync(target, { recursive: true, force: true });
    }
  }

  fs.mkdirSync(target, { recursive: true });
  for (const entry of ENTRIES) {
    copyRecursive(path.join(PACKAGE_ROOT, entry), path.join(target, entry));
  }

  console.log("工程化提示词优化 installed.");
  console.log(`Target: ${target}`);
  console.log("Restart Codex or reload the session so the skill list refreshes.");
}

try {
  const args = parseArgs(process.argv.slice(2));
  installSkill(args.target, args.backup);
} catch (error) {
  console.error(`Install failed: ${error.message}`);
  console.error("");
  console.error(usage());
  process.exit(1);
}

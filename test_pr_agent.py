#!/usr/bin/env python3
"""
Test script to verify PR Integration Agent configuration
"""
import os
import sys
import yaml
import json


def test_workflow_files():
    """Test that workflow files exist and are valid YAML"""
    print("🔍 Testing workflow files...")
    
    workflows = [
        '.github/workflows/pr-integration-agent.yml',
        '.github/workflows/docker-deployment.yml',
        '.github/workflows/verify.yml'
    ]
    
    for workflow in workflows:
        if not os.path.exists(workflow):
            print(f"❌ Missing workflow: {workflow}")
            return False
            
        try:
            with open(workflow, 'r') as f:
                yaml.safe_load(f)
            print(f"✅ Valid workflow: {workflow}")
        except Exception as e:
            print(f"❌ Invalid YAML in {workflow}: {e}")
            return False
    
    return True


def test_config_files():
    """Test that configuration files exist"""
    print("\n🔍 Testing configuration files...")
    
    configs = [
        '.pylintrc',
        '.flake8',
        'pyproject.toml',
        'CONTRIBUTING.md',
        '.github/PR_INTEGRATION_AGENT.md',
        '.github/PULL_REQUEST_TEMPLATE/pull_request_template.md'
    ]
    
    for config in configs:
        if not os.path.exists(config):
            print(f"❌ Missing config: {config}")
            return False
        print(f"✅ Found config: {config}")
    
    return True


def test_pyproject_toml():
    """Test that pyproject.toml is valid TOML"""
    print("\n🔍 Testing pyproject.toml...")
    
    try:
        # Try tomllib first (Python 3.11+)
        try:
            import tomllib
            with open('pyproject.toml', 'rb') as f:
                tomllib.load(f)
        except ImportError:
            # Fall back to toml for older Python versions
            try:
                import toml
                with open('pyproject.toml', 'r') as f:
                    toml.load(f)
            except ImportError:
                print("⚠️  Neither tomllib nor toml module available, skipping validation")
                return True
        
        print("✅ Valid pyproject.toml")
        return True
    except Exception as e:
        print(f"❌ Invalid pyproject.toml: {e}")
        return False


def test_pr_template():
    """Test that PR template has required sections"""
    print("\n🔍 Testing PR template...")
    
    template_path = '.github/PULL_REQUEST_TEMPLATE/pull_request_template.md'
    
    try:
        with open(template_path, 'r') as f:
            content = f.read()
        
        required_sections = [
            'Description',
            'Type de changement',
            'Tests',
            'Checklist'
        ]
        
        for section in required_sections:
            if section not in content:
                print(f"❌ Missing section in PR template: {section}")
                return False
        
        print("✅ PR template has all required sections")
        return True
    except Exception as e:
        print(f"❌ Error reading PR template: {e}")
        return False


def test_workflow_structure():
    """Test that PR integration workflow has required jobs"""
    print("\n🔍 Testing PR integration workflow structure...")
    
    try:
        with open('.github/workflows/pr-integration-agent.yml', 'r') as f:
            workflow = yaml.safe_load(f)
        
        required_jobs = [
            'validate-pr-rules',
            'code-quality',
            'test-with-coverage',
            'manage-labels',
            'pr-summary'
        ]
        
        jobs = workflow.get('jobs', {})
        
        for job in required_jobs:
            if job not in jobs:
                print(f"❌ Missing job in workflow: {job}")
                return False
        
        print("✅ Workflow has all required jobs")
        return True
    except Exception as e:
        print(f"❌ Error validating workflow structure: {e}")
        return False


def main():
    """Run all tests"""
    print("=" * 60)
    print("🤖 PR Integration Agent Configuration Test")
    print("=" * 60)
    
    tests = [
        test_workflow_files,
        test_config_files,
        test_pyproject_toml,
        test_pr_template,
        test_workflow_structure
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"❌ Test failed with error: {e}")
            results.append(False)
    
    print("\n" + "=" * 60)
    if all(results):
        print("✅ All tests passed!")
        print("=" * 60)
        return 0
    else:
        print("❌ Some tests failed!")
        print("=" * 60)
        return 1


if __name__ == '__main__':
    sys.exit(main())

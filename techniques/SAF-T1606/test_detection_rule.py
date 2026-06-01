#!/usr/bin/env python3
"""
Test script for SAF-T1606 Directory Listing via File Tool detection rule validation.

This script validates that our detection rule correctly identifies attempts to list
contents of sensitive system directories via MCP tools from the test log data.
"""

__author__ = "Vikranth Kumar Shivaa"

import json
import os
from typing import List, Dict, Any

class DirectoryListingDetector:
    """Detector for Directory Listing activities based on SAF-T1606 rule."""
    
    def __init__(self):
        self.suspicious_tools = ['list_directory', 'ls', 'dir', 'filesystem_list_directory']
        self.sensitive_paths = ['/etc', '/root', 'C:\\Windows', 'C:\\Users\\Administrator', '.ssh', '.aws', '.env']
        
    def detect_suspicious_listing(self, events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Detect suspicious directory listing attempts."""
        detections = []
        
        for event in events:
            tool_name = event.get('tool_name', '')
            parameters = event.get('parameters', {})
            path = parameters.get('path', '')
            
            if tool_name in self.suspicious_tools:
                if any(sensitive in path for sensitive in self.sensitive_paths):
                    detections.append({
                        'detection_type': 'suspicious_directory_listing',
                        'timestamp': event.get('timestamp'),
                        'tool_name': tool_name,
                        'path': path,
                        'severity': 'medium',
                        'description': f'Suspicious directory listing detected: {tool_name} called on {path}'
                    })
        
        return detections
    
    def analyze_logs(self, log_file: str) -> Dict[str, Any]:
        """Analyze log file for directory listing activities."""
        try:
            with open(log_file, 'r') as f:
                events = json.load(f)
        except Exception as e:
            return {'error': f'Failed to load log file: {e}'}
        
        all_detections = []
        
        # Run detection
        all_detections.extend(self.detect_suspicious_listing(events))
        
        # Categorize by severity
        critical = [d for d in all_detections if d.get('severity') == 'critical']
        high = [d for d in all_detections if d.get('severity') == 'high']
        medium = [d for d in all_detections if d.get('severity') == 'medium']
        
        return {
            'total_events': len(events),
            'total_detections': len(all_detections),
            'detections': {
                'critical': critical,
                'high': high,
                'medium': medium
            },
            'summary': {
                'critical_count': len(critical),
                'high_count': len(high),
                'medium_count': len(medium),
                'detection_types': list(set([d['detection_type'] for d in all_detections]))
            }
        }

def main():
    """Main function to test directory listing detection."""
    detector = DirectoryListingDetector()
    
    # Test with our sample log data
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_file = os.path.join(script_dir, 'test-logs.json')
    
    results = detector.analyze_logs(log_file)
    
    if 'error' in results:
        print(f"❌ Error: {results['error']}")
        return
    
    print("🔍 SAF-T1606 Directory Listing Detection Results")
    print("=" * 60)
    print(f"📊 Total Events Analyzed: {results['total_events']}")
    print(f"🚨 Total Detections: {results['total_detections']}")
    print()
    
    summary = results['summary']
    print("📈 Detection Summary:")
    print(f"  🔴 Critical: {summary['critical_count']}")
    print(f"  🟠 High: {summary['high_count']}")
    print(f"  🟡 Medium: {summary['medium_count']}")
    print()
    
    print("🎯 Detection Types Found:")
    for detection_type in summary['detection_types']:
        print(f"  • {detection_type}")
    print()
    
    # Show detailed detections
    detections = results['detections']
    
    if detections['medium']:
        print("🟡 MEDIUM SEVERITY DETECTIONS:")
        for detection in detections['medium']:
            print(f"  ⚠️  {detection['description']}")
        print()
    
    print("✅ Detection rule validation complete!")

if __name__ == '__main__':
    main()


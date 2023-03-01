#!/bin/bash

# Set the start and end dates for the time period of cost report
start_date=$(date +%Y-%m-01)
end_date=$(date -d "$(date +%Y-%m-01) +1 month -1 day" +%Y-%m-%d)

# Get the cost and usage report by resource,the level of granularity (e.g., hourly, daily, or monthly). Check this doc for more info https://docs.aws.amazon.com/cli/latest/reference/ce/get-cost-and-usage.html
usage_report=$(aws ce get-cost-and-usage --time-period Start=$start_date,End=$end_date --granularity MONTHLY --metrics "BlendedCost" "UnblendedCost" "UsageQuantity" --group-by Type=DIMENSION,Key=SERVICE --query 'ResultsByTime[0].Groups')

# Verify if the cost and usage report retrieval was successful
if [ -z "$usage_report" ]; then
  echo "Error: To retrieve cost and usage information by resource."
  exit 1
fi

# Format the usage and cost report by resource as a table
report_table=$(echo "$usage_report" | jq -r '.[] | [.Keys[0], .Metrics.BlendedCost.Amount, .Metrics.UnblendedCost.Amount, .Metrics.UsageQuantity.Amount] | @tsv' | column -t -s $'\t' | awk 'BEGIN { print "Resource\tBlendedCost\tUnblendedCost\tUsageQuantity" } { print }')

# Check if the EC2 or S3 resource usage exceeds $5
if echo "$report_table" | grep -E '(^AmazonEC2|^AmazonS3)' | awk -F '\t' '$2 > 5 || $3 > 5'; then
  # Send an email with the cost and usage report by resource(Don't forget to verify the email address: https://docs.aws.amazon.com/cli/latest/reference/ses/send-email.html)
  aws ses send-email --from "sender@example.com" --to "recipient@example.com" --subject "AWS cost and usage report for the month" --text "$(echo "$report_table")"
fi

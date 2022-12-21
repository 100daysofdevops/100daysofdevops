# Create a list of options for Kubernetes Debugging
options=("CrashLoopBackOff" "ImagePullBackOff" "ContainerCreating" "CreateContainerConfigError" "Quit")

# Display the menu and prompt the user to select an option
echo "Please select from the following Kubernetes Debugging option"
PS3="Please select an option: "
select opt in "${options[@]}"; do
    # Process the user's selection
    case $opt in
        "CrashLoopBackOff")
            # Execute crash_loopback_error.sh
            source crash_loopback_error.sh
            ;;
        "ImagePullBackOff")
            # Execute pod_image_pull_error.sh
            source pod_image_pull_error.sh
            ;;
        "ContainerCreating")
            # Execute container_creating_error.sh
            source container_creating_error.sh
            ;;
        "CreateContainerConfigError")
            # Execute create_container_config.sh
            source create_container_config.sh
            ;;                         
        "Quit")
            break
            ;;
        *) echo "Invalid option. Please try again.";;
    esac
done
